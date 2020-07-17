<template>
  <ValidationProvider
    v-slot="{ errors, valid }"
    :vid="vid"
    :name="$attrs.label"
    :rules="rules"
  >
    <b-field
      v-bind="$attrs"
      :type="{ 'is-danger': errors[0], 'is-success': valid }"
      :message="errors"
      horizontal
    >
      <b-select v-model="innerValue" :icon="icon" placeholder="placeholder">
        <slot />
      </b-select>
    </b-field>
  </ValidationProvider>
</template>

<script>
import { ValidationProvider } from 'vee-validate'

export default {
  components: {
    ValidationProvider
  },
  props: {
    vid: {
      type: String,
      default: null
    },
    placeholder: {
      type: String,
      default: ''
    },
    rules: {
      type: [Object, String],
      default: ''
    },
    icon: {
      type: String,
      default: ''
    },
    value: {
      type: null,
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
