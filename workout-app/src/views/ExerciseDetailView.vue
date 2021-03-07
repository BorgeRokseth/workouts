<template>
  <v-container>
    <v-card>
      <v-card-title>
        Exercise Details
      </v-card-title>
      <v-card-text v-if="exercise !== null">
        <v-text-field v-model="exercise.name" label="Name" />
        <v-textarea auto-grow v-model="exercise.description" label="Name" />
        Silent:
        <v-radio-group v-model="exercise.silent" row>
          <v-radio label="Yes!" :value="true"></v-radio>
          <v-radio label="No!" :value="false"></v-radio>
        </v-radio-group>
        Equipment:
        <v-radio-group v-model="exercise.equipment" row>
          <v-radio label="Yes, you need equipment!" :value="true"></v-radio>
          <v-radio label="No equipment needed!" :value="false"></v-radio>
        </v-radio-group>
        <v-select
          v-model="exercise.type"
          :items="typeItems"
          label="Type"
        ></v-select>
      </v-card-text>
      <v-card-actions>
        <v-btn @click="updateExercise(exercise)" dark>
          SAVE
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import { Exercise } from "@/api/Exercise";
import axios, { AxiosResponse } from "axios";

@Component
export default class ExerciseDetailView extends Vue {
  exercise: Exercise | null = null;
  errorMsg = " ";
  typeItems = ["Cardio", "Strength", "Stretch"];

  async mounted() {
    try {
      const exerciseId = parseInt(this.$route.params.exerciseId);
      await Promise.all([
        axios
          .get(`http://127.0.0.1:8095/api/exercises/${exerciseId}`)
          .then(res => (this.exercise = res.data))
      ]);
    } catch (e) {
      this.errorMsg = `Unable to fetch exercise (error ${e}`;
    }
  }

  updateExercise(data: Exercise): Promise<AxiosResponse<Exercise>> {
    if (this.exercise.id !== null) {
      return axios
          .put<Exercise>(
              `http://127.0.0.1:8095/api/exercises/${this.exercise.id}/`,
              data
          )
          .then(res =>
              axios.get(`http://127.0.0.1:8095/api/exercises/${res.data.id}`)
          )
          .then(res => (this.exercise = res.data));
    }
  }
}
</script>

<style scoped></style>
