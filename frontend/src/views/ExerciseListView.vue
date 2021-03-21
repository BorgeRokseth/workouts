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
    </v-card>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service";

export default {
  name: "ExerciseListView",
  data() {
    return {
      exercises: []
    };
  },
  methods: {
    getExercises() {
      const endpoint = "/api/exercises/";
      apiService(endpoint).then(data => {
        this.exercises.push(...data);
      });
    },
    getAnswer(state) {
      if (state) return "Yes";
      return "No";
    }
  },
  created() {
    this.getExercises();
    document.title = "WorkoutFlows";
  }
};
</script>

<style scoped></style>
