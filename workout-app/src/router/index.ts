import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import ExerciseListView from "@/views/ExerciseListView.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/exercises",
    name: "Exercises",
    component: ExerciseListView
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
