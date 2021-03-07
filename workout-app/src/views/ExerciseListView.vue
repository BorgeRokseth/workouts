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
          <tr v-for="item in exercises" :key="item.id">
            <td>
              <router-link
                :to="{
                  name: 'exercise details',
                  params: { exerciseId: item.id }
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
        <v-btn @click="addDummyComponent">
          ADD
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
export default class ExerciseListView extends Vue {
  title = "Exersice list view";
  exercises: Exercise[] | null = null;
  errorMsg = " ";

  dummyData: Exercise = {
    name: "New Exercise",
    description: "No description",
    silent: false,
    equipment: false,
    type: "Strength",
    author: 1
  };
  editComponent = false;

  mounted() {
    Promise.all([
      axios
        .get("http://127.0.0.1:8095/api/exercises/")
        .then(res => (this.exercises = res.data))
        .catch(e => {
          this.errorMsg = `Unable to fetch exercises (error ${e}`;
        })
    ]);
  }
  getAnswer(state: boolean) {
    if (state) return "Yes";
    return "No";
  }

  addDummyComponent(): Promise<AxiosResponse<Exercise>> {
    return axios
      .post<Exercise>(`http://127.0.0.1:8095/api/exercises/`, this.dummyData)
      .then(res => {
        if (this.exercises !== null) {
          this.exercises.push(res.data);
        }
      });
  }
}
</script>

<style scoped></style>

