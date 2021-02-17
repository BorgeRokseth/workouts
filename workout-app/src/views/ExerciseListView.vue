<template>
  <div>
    <h3>{{ title }}</h3>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";

@Component
export default class ExerciseListView extends Vue {
  title = "Exersice list view";
}
</script>

<style scoped></style>
