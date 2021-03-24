<template>
  <v-container>
    <v-card>
      <v-card-title>
        Exercises
      </v-card-title>
      <v-simple-table>
        <thead>
          <tr>
            <th class="text-left">
              Name
            </th>
            <th class="text-left">
              Silent
            </th>
            <th class="text-left">
              Equipment
            </th>
            <th class="text-left">
              Type
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item of exercises" :key="item.id">
            <td>
              <router-link
                :to="{
                  name: 'Exercise details',
                  params: { id: item.id }
                }"
              >
                {{ item.name }}
              </router-link>
            </td>
            <td>{{ getAnswer(item.silent) }}</td>
            <td>{{ getAnswer(item.equipment) }}</td>
            <td>{{ item.type }}</td>
          </tr>
        </tbody>
      </v-simple-table>
      <v-card-actions>
        <v-btn @click="createNewExercise">
          <v-icon> mdi-plus-box </v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
    <EditExerciseDialog
      :show-dialog="showNewExerciseDialog"
      :id="newExerciseId"
      @close:dialog="closeNewExerciseDialog"
      @refresh:exercise="getExercises"
    />
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service";
import EditExerciseDialog from "@/components/EditExerciseDialog";

export default {
  name: "ExerciseListView",
  components: {
    EditExerciseDialog
  },
  data() {
    return {
      exercises: [],
      showNewExerciseDialog: false,
      newExerciseId: 1,
      user: null
    };
  },
  methods: {
    getExercises() {
      const endpoint = "/api/exercises/";
      apiService(endpoint).then(data => {
        this.exercises = data;
      });
    },
    getUserDetails() {
      const endpoint = "/api/user/";
      apiService(endpoint).then(data => {
        this.user = data.username;
      });
    },
    createExercise(exercise) {
      const endpoint = "/api/exercises/";
      apiService(endpoint, "POST", { content: exercise }).then(data => {
        this.newExercise = data;
        this.newExerciseId = data.id;
      });
    },
    getAnswer(state) {
      if (state) return "Yes";
      return "No";
    },
    createNewExercise() {
      const newExercise = {
        name: "New Exercise",
        description: "Describe the exercise",
        silent: true,
        equipment: true,
        type: "Cardio",
        author: this.user
      };
      this.createExercise(newExercise);
      this.showNewExerciseDialog = true;
    },
    closeNewExerciseDialog(){
      this.getExercises()
      this.showNewExerciseDialog = false
    }
  },
  created() {
    this.getExercises();
    this.getUserDetails();
    document.title = "WorkoutFlows";
  }
};
</script>

<style scoped></style>
