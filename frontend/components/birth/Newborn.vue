<template>
  <div>
    <v-input rules="required" label="teste" :value="newborn.name" @input="updateName" />
    <v-input rules="required" label="teste2" :value="newborn.weight" @input="updateWeight" />
  </div>
</template>

<script>
import VInput from '@/components/templates/VInput'
export default {
  components: { VInput },
  props: {
    newborn: Object,
    index: Number,
  },
  methods: {
    updateName(name) {
      this.$store.commit('birth/newbornName', {name, index: this.index})
    },
    updateWeight(weight) {
      this.$store.commit('birth/newbornWeight', {weight, index: this.index})
    }
  }
  // }


}
</script>

<style>
</style>
