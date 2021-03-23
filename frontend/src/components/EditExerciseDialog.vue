<template>
  <v-row justify="center">
    <v-dialog v-model="showDialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Edit Exercise</span>
        </v-card-title>
        <v-card-text>
          <v-text-field
            label="Name of Exercise"
            v-model="newName"
          ></v-text-field>
          <v-textarea
            label="Exercise Description"
            v-model="newDescription"
          ></v-textarea>
          <v-row>
            <v-col>
              Silent:
              <v-radio-group v-model="silent" row>
                <v-radio label="Yes!" :value="true"></v-radio>
                <v-radio label="No!" :value="false"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col>
              Equipment:
              <v-radio-group v-model="equipment" row>
                <v-radio
                  label="Yes, you need equipment!"
                  :value="true"
                ></v-radio>
                <v-radio label="No equipment needed!" :value="false"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col>
              <v-select
                v-model="typeOfExercise"
                :items="typeItems"
                label="Type"
              ></v-select>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDialog">
            Close
          </v-btn>
          <v-btn color="blue darken-1" text @click="save">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { apiService } from "@/common/api.service";

export default {
  name: "EditExerciseDialog",
  props: {
    id: Number,
    showDialog: Boolean
  },
  data() {
    return {
      exercise: {},
      dialog: true,
      newName: " ",
      newDescription: " ",
      silent: true,
      equipment: true,
      typeOfExercise: "Cardio",
      typeItems: ["Cardio", "Strength", "Stretch"]
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
      });
    },
    getAnswer(state) {
      if (state) return "Yes";
      return "No";
    },
    closeDialog() {
      this.$emit("close:dialog", {});
    },
    updateExercise(exercise) {
      const endpoint = `/api/exercises/${this.id}/`;
      apiService(endpoint, "PUT", { content: exercise }).then(data => {
        this.exercise = data;
      });
    },
    save() {
      const exerciseUpdates = {
        name: this.newName,
        description: this.newDescription,
        silent: this.silent,
        equipment: this.equipment,
        type: this.typeOfExercise
      };
      console.log(exerciseUpdates);
      this.updateExercise(exerciseUpdates);
      this.closeDialog();
    }
  },
  created() {
    this.getExerciseDetails();
  }
};
</script>

<style scoped></style>
