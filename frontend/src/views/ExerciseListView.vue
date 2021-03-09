<template>
  <v-container>
    <v-card>
      <v-card-title>
        Exercises
      </v-card-title>
      <v-card-text>
        {{ errorMsg }}
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";

@Component
export default class ExerciseListView extends Vue {
  errorMsg = "Hello Vue";
}
</script>

<style scoped></style>
