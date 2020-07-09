<template>
  <section>
    <div class="form">
      <input type="hidden" id="sheep-id" v-model="sheep.id" />
      <b-field
        :label="$t('pages.admin.sheep.forms.earringNumber.label')"
        class="sheep-form-fields"
      >
        <b-input
          :placeholder="$t('pages.admin.sheep.forms.earringNumber.placeholder')"
          type="text"
          icon="tag"
          v-model="sheep.earringNumber"
          :readonly="mode === 'remove'"
          required
        />
      </b-field>
      <b-field
        :label="$t('pages.admin.sheep.forms.breed.label')"
        class="sheep-form-fields"
      >
        <b-select
          :placeholder="$t('pages.admin.sheep.forms.breed.placeholder')"
          icon="puzzle"
          v-model="sheep.breed"
          :readonly="mode === 'remove'"
          required
        >
          <option v-for="breed in breeds" :value="breed.id" :key="breed.id">{{
            breed.name
          }}</option>
        </b-select>
      </b-field>
      <b-field
        :label="$t('pages.admin.sheep.forms.category.label')"
        class="sheep-form-fields"
      >
        <b-select
          :placeholder="$t('pages.admin.sheep.forms.category.placeholder')"
          icon="alpha-c-circle-outline"
          v-model="sheep.category"
          :readonly="mode === 'remove'"
          required
        >
          <option
            v-for="category in categories"
            :value="category.id"
            :key="category.id"
            >{{ category.name }}</option
          >
        </b-select>
      </b-field>
      <b-field
        :label="$t('pages.admin.sheep.forms.birthday.label')"
        class="sheep-form-fields"
      >
        <b-datepicker
          :placeholder="$t('pages.admin.sheep.forms.birthday.placeholder')"
          icon="calendar-today"
          v-model="birthday"
          :readonly="mode === 'remove'"
        />
      </b-field>
      <b-field
        :label="$t('pages.admin.sheep.forms.sex.label')"
        class="sheep-form-fields"
      >
        <b-radio v-model="sheep.sex" name="form-sex" native-value="M">{{
          $t('pages.admin.sheep.forms.sex.male')
        }}</b-radio>
        <b-radio v-model="sheep.sex" name="form-sex" native-value="F">{{
          $t('pages.admin.sheep.forms.sex.female')
        }}</b-radio>
      </b-field>
      <div class="sheep-form-buttons">
        <b-button type="is-info" icon-left="check" @click="save">{{
          $t('buttons.save')
        }}</b-button>
        <b-button type="is-dark" icon-left="redo" @click="reset">{{
          $t('buttons.reset')
        }}</b-button>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    value: Object
  },
  data() {
    return {
      categories: [],
      breeds: [],
      sheep: {},
      birthday: ''
    }
  },
  async fetch() {
    this.categories = await this.$axios.$get('/api/v1/categories')
    this.breeds = await this.$axios.$get('/api/v1/breeds')
    this.sheep = {
      id: this.value.id,
      earringNumber: this.value.earringNumber,
      breed: this.breeds.find(elem => elem.name == this.value.breed).id,
      category: this.categories.find(elem => elem.name == this.value.category)
        .id,
      birthday: this.value.birthday,
      sex: this.value.sex == 'Male' ? 'M' : 'F',
      teethQuantity: this.value.teethQuantity,
      lactating: this.value.lactating
    }
    this.birthday = new Date(this.sheep.birthday)
  },
  methods: {
    reset() {
      this.sheep = {
        id: this.value.id,
        earringNumber: this.value.earringNumber,
        breed: this.breeds.find(elem => elem.name == this.value.breed).id,
        category: this.categories.find(elem => elem.name == this.value.category)
          .id,
        birthday: this.value.birthday,
        sex: this.value.sex == 'Male' ? 'M' : 'F',
        teethQuantity: this.value.teethQuantity,
        lactating: this.value.lactating
      }
      this.birthday = new Date(this.sheep.birthday)
    },
    save() {
      const url = `/api/v1/sheeps/${this.sheep.id}/`
      this.sheep.birthday = this.birthday.toLocaleDateString('fr-CA')
      this.$axios['patch'](url, this.sheep)
        .then(() => {
          this.$toasted.global.defaultSuccess()
          // this.reset()
        })
        .catch(e => {
          for (var item in e.response.data) {
            this.$toast.error(item + ': ' + e.response.data[item])
          }
        })
    }
  }
}
</script>

<style></style>
