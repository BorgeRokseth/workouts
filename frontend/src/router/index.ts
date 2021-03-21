import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import ExerciseListView from "@/views/ExerciseListView.vue";
import FlowListView from "@/views/FlowListView.vue";
import WorkoutListView from "@/views/WorkoutListView.vue";
import ExerciseDetailView from "@/views/ExerciseDetailView.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/exercises",
    name: "Exercises",
    component: ExerciseListView
  },
  {
    path: "/exercises/:id",
    name: "Exercise details",
    component: ExerciseDetailView,
    props: true
  },
  {
    path: "/flows",
    name: "Flows",
    component: FlowListView
  },
  {
    path: "/workouts",
    name: "Workouts",
    component: WorkoutListView
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
