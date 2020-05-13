<template>
  <div>
    <v-input
      rules="required"
      icon="tag"
      :label="$t('pages.admin.sheep.forms.earringNumber.label')"
      :value="newborn.earringNumber"
      @input="updateName"
    />

    <v-select
      :placeholder="$t('pages.admin.sheep.forms.breed.placeholder')"
      icon="puzzle"
      rules="required"
      :label="$t('pages.admin.sheep.forms.breed.label')"
      :value="newborn.breed"
      @input="updateName"
    >
      <option v-for="breed in breeds" :value="breed.id" :key="breed.id">{{ breed.name }}</option>
    </v-select>

    <v-select
      :placeholder="$t('pages.admin.sheep.forms.category.placeholder')"
      icon="alpha-c-circle-outline"
      rules="required"
      :label="$t('pages.admin.sheep.forms.category.label')"
      :value="newborn.category"
      @input="updateName"
    >
      <option
        v-for="category in categories"
        :value="category.id"
        :key="category.id"
      >{{ category.name }}</option>
    </v-select>

    <b-field :label="$t('pages.admin.sheep.forms.sex.label')" class="sheep-form-fields">
      <b-radio
        v-model="newborn.sex"
        name="form-sex"
        native-value="M"
      >{{ $t('pages.admin.sheep.forms.sex.male') }}</b-radio>
      <b-radio
        v-model="newborn.sex"
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
