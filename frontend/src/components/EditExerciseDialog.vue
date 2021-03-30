<template>
  <v-row justify="center">
    <v-dialog v-model="showDialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Edit Exercise</span>
        </v-card-title>
        <v-card-text>
          <v-text-field
            v-if="exerciseToEdit"
            label="Name of Exercise"
            v-model="exercise.name"
          ></v-text-field>
          <v-text-field
            v-else
            label="Name of Exercise"
            v-model="newName"
          ></v-text-field>
          <v-textarea
            v-if="exerciseToEdit"
            label="Exercise Description"
            v-model="exercise.description"
          ></v-textarea>
          <v-textarea
            v-else
            label="Exercise Description"
            v-model="newDescription"
          ></v-textarea>
          <v-row>
            <v-col v-if="exerciseToEdit">
              Silent:
              <v-radio-group v-model="exercise.silent" col>
                <v-radio label="Yes!" :value="true"></v-radio>
                <v-radio label="No!" :value="false"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col v-else>
              Silent:
              <v-radio-group v-model="silent" column>
                <v-radio label="Yes!" :value="true"></v-radio>
                <v-radio label="No!" :value="false"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col v-if="exerciseToEdit">
              <v-select
                v-model="exercise.equipment"
                :items="availableEquipment"
                name="Equipment"
                label="Equipment"
                item-text="name"
                item-value="id"
                multiple
                chips
              >
              </v-select>
            </v-col>
            <v-col v-else>
              <v-select
                v-model="selectedEquipment"
                :items="availableEquipment"
                name="Equipment"
                label="Equipment"
                item-text="name"
                item-value="id"
                multiple
                chips
              >
              </v-select>
            </v-col>
            <v-col v-if="exerciseToEdit">
              <v-select
                v-model="exercise.type"
                :items="typeItems"
                label="Type"
              ></v-select>
            </v-col>
            <v-col v-else>
              <v-select
                v-model="typeOfExercise"
                :items="typeItems"
                label="Type"
              ></v-select>
            </v-col>
          </v-row>
          <v-card>
            <v-card-subtitle>
              Add New Equipment:
            </v-card-subtitle>
            <v-card-text>
              <v-row>
                <v-col>
                  <v-text-field
                    label="Equipment Name"
                    v-model="newEquipmentName"
                  />
                </v-col>
                <v-col>
                  <v-text-field
                    label="Comment / Description"
                    v-model="newEquipmentDescription"
                  />
                </v-col>
              </v-row>
            </v-card-text>
            <v-card-actions>
              <v-btn @click="saveNewEquipment"> Add</v-btn>
            </v-card-actions>
          </v-card>
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
    showDialog: Boolean,
    exerciseToEdit: {
      id: Number,
      name: String,
      description: String,
      silent: Boolean,
      equipment: Array,
      typeOfExercise: String,
      author: String
    },
    user: Number
  },
  data() {
    return {
      exercise: this.exerciseToEdit,
      dialog: true,
      newName: " ",
      newDescription: " ",
      silent: true,
      typeOfExercise: "Cardio",
      typeItems: ["Cardio", "Strength", "Stretch"],
      availableEquipment: [],
      availableEquipmentNames: [],
      selectedEquipment: [],
      newEquipmentName: " ",
      newEquipmentDescription: " "
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
    getAvailableEquipment() {
      const endpoint = "/api/equipment/";
      apiService(endpoint).then(data => {
        this.availableEquipment = data;
        this.getAvailableEquipmentNames();
      });
    },
    createEquipment(equipment) {
      const endpoint = "/api/equipment/";
      const method = "POST";
      apiService(endpoint, method, equipment).then(data => {
        this.getAvailableEquipment();
        if (this.exerciseToEdit) {
          this.exercise.equipment.push(data.id);
        } else {
          this.selectedEquipment.push(data.id);
        }
      });
    },
    getAvailableEquipmentNames() {
      this.availableEquipmentNames = this.availableEquipment.map(equipment => {
        return equipment.name;
      });
    },
    getAnswer(state) {
      if (state) return "Yes";
      return "No";
    },
    closeDialog() {
      this.$emit("refresh:exercise", {});
      this.$emit("close:dialog", {});
    },
    updateExercise(exercise) {
      const endpoint = `/api/exercises/${this.id}/`;
      apiService(endpoint, "PUT", { content: exercise }).then(data => {
        this.exercise = data;
      });
    },
    save() {
      this.getAvailableEquipment();
      if (this.exerciseToEdit) {
        const exerciseUpdates = {
          name: this.exercise.name,
          description: this.exercise.description,
          silent: this.exercise.silent,
          equipment: this.exercise.equipment,
          type: this.exercise.type
        };
        this.updateExercise(exerciseUpdates);
        this.getExerciseDetails();
      } else {
        const exerciseUpdates = {
          name: this.newName,
          description: this.newDescription,
          silent: this.silent,
          equipment: this.selectedEquipment,
          type: this.typeOfExercise
        };
        this.updateExercise(exerciseUpdates);
        this.getExerciseDetails();
      }
      this.$emit("refresh:exercise", {});
      this.closeDialog();
    },
    saveNewEquipment() {
      const newEquipment = {
        name: this.newEquipmentName,
        description: this.newEquipmentDescription,
        author: this.user
      };
      this.createEquipment(newEquipment);
    }
  },
  created() {
    this.getExerciseDetails();
    this.getAvailableEquipment();
  }
};
</script>

<style scoped></style>
