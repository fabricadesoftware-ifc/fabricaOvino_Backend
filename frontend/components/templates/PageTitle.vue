<template>
  <div class="page-title">
    <h1 class="title is-2"><b-icon v-if="icon" :icon="icon" size="is-medium"></b-icon> {{ main }}</h1>
    <h2 class="subtitle is-4">{{ sub }}</h2>
    <hr />
  </div>
</template>

<script>
export default {
  name: "PageTitle",
  props: ["icon", "main", "sub"],
};
</script>

<style></style>
