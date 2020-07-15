<template>
  <div class="page-title">
    <h1 class="title is-2">
      <b-icon v-if="icon" :icon="icon" size="is-medium"></b-icon> {{ main }}
    </h1>
    <h2 class="subtitle is-4">{{ sub }}</h2>
    <hr />
  </div>
</template>

<script>
export default {
  props: {
    icon: {
      type: String,
      default: null
    },
    main: {
      type: String,
      default: null
    },
    sub: {
      type: String,
      default: null
    }
  }
}
</script>

<style></style>
