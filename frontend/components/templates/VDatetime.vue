<template>
  <b-field :label="label" horizontal>
    <b-datetimepicker v-model="innerValue" icon="calendar-today">
      <template v-slot:left>
        <button class="button is-primary" @click="innerValue = new Date()">
          <b-icon icon="clock"></b-icon>
          <span>{{ $t('buttons.now') }}</span>
        </button>
      </template>
      <template v-slot:right>
        <button class="button is-danger" @click="innerValue = null">
          <b-icon icon="close"></b-icon>
          <span>{{ $t('buttons.clear') }}</span>
        </button>
      </template>
    </b-datetimepicker>
  </b-field>
</template>

<script>
export default {
  props: {
    value: {
      type: null,
      default: null
    },
    label: {
      type: String,
      default: null
    }
  },
  data() {
    return {
      innerValue: ''
    }
  },
  watch: {
    innerValue(newVal) {
      this.$emit('input', newVal)
    },
    value(newVal) {
      this.innerValue = newVal
    }
  },
  created() {
    if (this.value) {
      this.innerValue = this.value
    }
  }
}
</script>

<style></style>
