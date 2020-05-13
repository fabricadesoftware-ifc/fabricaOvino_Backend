<template>
  <div>
    <v-input
      rules="required"
      icon="tag"
      :label="$t('pages.admin.sheep.forms.earringNumber.label')"
      :value="newborn.earringNumber"
      @input="updateEarringNumber"
    />

    <v-select
      :placeholder="$t('pages.admin.sheep.forms.breed.placeholder')"
      icon="puzzle"
      rules="required"
      :label="$t('pages.admin.sheep.forms.breed.label')"
      :value="newborn.breed"
      @input="updateBreed"
    >
      <option v-for="breed in breeds" :value="breed.id" :key="breed.id">{{ breed.name }}</option>
    </v-select>

    <v-select
      :placeholder="$t('pages.admin.sheep.forms.category.placeholder')"
      icon="alpha-c-circle-outline"
      rules="required"
      :label="$t('pages.admin.sheep.forms.category.label')"
      :value="newborn.category"
      @input="updateCategory"
    >
      <option
        v-for="category in categories"
        :value="category.id"
        :key="category.id"
      >{{ category.name }}</option>
    </v-select>

    <b-field :label="$t('pages.admin.sheep.forms.sex.label')">
      <b-radio
        :value="newborn.sex"
        @input="updateSex"
        name="form-sex"
        native-value="M"
      >{{ $t('pages.admin.sheep.forms.sex.male') }}</b-radio>
      <b-radio
        :value="newborn.sex"
        @input="updateSex"
        name="form-sex"
        native-value="F"
      >{{ $t('pages.admin.sheep.forms.sex.female') }}</b-radio>
    </b-field>

    <v-input rules="required" label="Peso" :value="newborn.weight" @input="updateWeight" />
  </div>
</template>

<script>
import VInput from '@/components/templates/VInput'
import VSelect from '@/components/templates/VSelect'
export default {
  data() {
    return {
      breeds: [],
      categories: []
    }
  },
  async fetch() {
    this.breeds = await this.$axios.$get("/api/v1/breeds")
    this.categories = await this.$axios.$get("/api/v1/categories")
  },
  components: { VInput, VSelect },
  props: {
    newborn: Object,
    index: Number,
  },
  methods: {
    updateEarringNumber(earringNumber) {
      this.$store.commit('birth/newbornEarringNumber', {earringNumber, index: this.index})
    },
    updateBreed(breed) {
      this.$store.commit('birth/newbornBreed', {breed, index: this.index})
    },
    updateCategory(category) {
      this.$store.commit('birth/newbornCategory', {category, index: this.index})
    },
    updateSex(sex) {
      this.$store.commit('birth/newbornSex', {sex, index: this.index})
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
