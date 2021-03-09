<template>
  <v-container>
    <v-card>
      <v-card-title>
        Exercise Details
      </v-card-title>
      <v-card-text >
        {{errorMsg}}
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";

@Component
export default class ExerciseDetailView extends Vue {
  errorMsg = "Hello Vue";
}
</script>

<style scoped></style>
