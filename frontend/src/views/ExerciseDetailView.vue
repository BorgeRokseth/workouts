<template>
  <v-container>
    <v-card>
      <v-card-title> Name: {{ exercise.name }} </v-card-title>
      <v-card-text>
        <v-row align="center" class="mx-3">
          <div class="my-4 subtitle-1">
            Description:
          </div>

          <v-container>{{ exercise.description }}</v-container>
        </v-row>
        <v-divider class="mx-4"></v-divider>
        <v-row align="center" class="mx-3">
          <v-col>
            <b>Silent: </b>
            <em>{{ getAnswer(exercise.silent) }}</em>
          </v-col>
          <v-col>
            <b>Equipment: </b>
            <em>{{ getAnswer(exercise.equipment) }}</em>
          </v-col>
          <v-col>
            <b>Type of exercise: </b>
            <em>{{ exercise.type }}</em>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-btn small @click="editExercise">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>

        <v-btn small @click="deleteExercise">
          <v-icon>mdi-trash-can-outline</v-icon>
        </v-btn>
        <EditExerciseDialog
            :show-dialog="showEditExerciseDialog"
            :id="id"
            :exercise-to-edit="exercise"
            @close:dialog="closeEditExerciseDialog"
            @refresh:exercise="getExerciseDetails"
        />
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service";
import EditExerciseDialog from "@/components/EditExerciseDialog";

export default {
  name: "ExerciseDetails",
  components: {
    EditExerciseDialog
  },
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      exercise: {},
      showEditExerciseDialog: false
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getExerciseDetails() {
      const endpoint = `/api/exercises/${this.id}/`;
      apiService(endpoint).then(data => {
        this.exercise = data;
        this.setPageTitle(data.name);
      });
    },
    getAnswer(state) {
      if (state) return "Yes";
      return "No";
    },
    editExercise(){
      this.showEditExerciseDialog = true;
    },
    closeEditExerciseDialog(){
      this.showEditExerciseDialog = false;
    },
    deleteExercise(){
      const endpoint = `/api/exercises/${this.id}/`;
      const method = "DELETE";
      apiService(endpoint, method).then();
      this.$router.push("/exercises")
    }
  },
  created() {
    this.getExerciseDetails();
  }
};
</script>

<style scoped></style>
