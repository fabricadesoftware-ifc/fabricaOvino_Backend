<template>
  <ValidationProvider :vid="vid" :name="$attrs.label" :rules="rules">
    <b-field
      slot-scope="{ errors, valid }"
      v-bind="$attrs"
      :type="{ 'is-danger': errors[0], 'is-success': valid }"
      :message="errors"
    >
      <b-select :icon="icon" placeholder="placeholder" v-model="innerValue">
        <slot />
      </b-select>
    </b-field>
  </ValidationProvider>
</template>

<script>
import { ValidationProvider } from "vee-validate";

export default {
  components: {
    ValidationProvider
  },
  props: {
    vid: {
      type: String
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
      type: null
    }
  },
  data: () => ({
    innerValue: ''
  }),
  watch: {
    innerValue (newVal) {
      this.$emit('input', newVal);
    },
    value (newVal) {
      this.innerValue = newVal;
    }
  },
  created () {
    if (this.value) {
      this.innerValue = this.value;
    }
  }
};
</script>
