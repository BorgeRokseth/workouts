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
          <v-col align-self="start">
            <b>Equipment: </b>
            <div v-for="equipment of exercise.equipment" :key="equipment">
              {{ getEquipmentName(equipment) }}
            </div>
          </v-col>
          <v-col align-self="start">
            <b>Silent: </b>
            <em>{{ getAnswer(exercise.silent) }}</em>
          </v-col>
          <v-col align-self="start">
            <b>Type of exercise: </b>
            <em>{{ exercise.type }}</em>
          </v-col>
        </v-row>
        <v-divider class="mx-4"></v-divider>
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
          :user="userId"
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
      showEditExerciseDialog: false,
      equipment: {},
      equipmentList: [],
      user: null,
      userId: null
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
    getEquipmentName(id) {
      if (
        this.equipmentList !== undefined &&
        this.equipmentList !== [] &&
        this.equipmentList !== null &&
        this.equipmentList.length !== null
      ) {
        const equipment = this.equipmentList.find(
          equipment => equipment.id === id
        );
        if (equipment !== undefined) {
          return equipment.name;
        }
      }
    },
    updateListOfEquipment() {
      const endpoint = "/api/equipment/";
      apiService(endpoint).then(data => {
        this.equipmentList = data;
      });
    },
    getAnswer(state) {
      if (state) return "Yes";
      return "No";
    },
    editExercise() {
      this.showEditExerciseDialog = true;
    },
    closeEditExerciseDialog() {
      this.updateListOfEquipment()
      this.getExerciseDetails();
      this.showEditExerciseDialog = false;
    },
    deleteExercise() {
      const endpoint = `/api/exercises/${this.id}/`;
      const method = "DELETE";
      apiService(endpoint, method).then();
      this.$router.push("/exercises");
    },
    getUserDetails() {
      const endpoint = "/api/user/";
      apiService(endpoint).then(data => {
        this.user = data.username;
        this.userId = data.id;
      });
    }
  },
  created() {
    this.getExerciseDetails();
    this.getUserDetails();
    this.updateListOfEquipment();
  }
};
</script>

<style scoped></style>
