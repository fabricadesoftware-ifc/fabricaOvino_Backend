<template>
  <b-datetimepicker v-model="date" icon="calendar-today">
    <template v-slot:left>
      <button class="button is-primary" @click="datetime = new Date()">
        <b-icon icon="clock"></b-icon>
        <span>{{ $t('buttons.now') }}</span>
      </button>
    </template>
    <template v-slot:right>
      <button class="button is-danger" @click="datetime = null">
        <b-icon icon="close"></b-icon>
        <span>{{ $t('buttons.clear') }}</span>
      </button>
    </template>
  </b-datetimepicker>
</template>

<script>
export default {
  // props: {
  //   label: String
  // },
  data() {
    return {
      date: new Date()
    }
  }
}
</script>

<style></style>
