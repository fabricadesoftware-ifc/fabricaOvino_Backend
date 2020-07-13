<template>
  <section>
    <b-button v-if="edit" type="is-dark" icon-left="redo" @click="reset()">{{
      $t('buttons.reset')
    }}</b-button>
    <b-button
      v-else
      type="is-warning"
      icon-left="pencil"
      @click="edit = !edit"
      >{{ $t('buttons.edit') }}</b-button
    >
    <hr />
    <div class="form">
      <input type="hidden" id="sheep-id" v-model="sheep.id" />
      <b-field :label="$t('pages.admin.sheep.forms.earringNumber.label')">
        <b-input
          :placeholder="$t('pages.admin.sheep.forms.earringNumber.placeholder')"
          type="text"
          icon="tag"
          v-model="sheep.earringNumber"
          :disabled="!edit"
          required
        />
      </b-field>
      <b-field :label="$t('pages.admin.sheep.forms.breed.label')">
        <b-select
          :placeholder="$t('pages.admin.sheep.forms.breed.placeholder')"
          icon="puzzle"
          v-model="sheep.breed"
          :disabled="!edit"
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
          :disabled="!edit"
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
      <b-field :label="$t('pages.admin.sheep.forms.birthday.label')">
        <b-datepicker
          :placeholder="$t('pages.admin.sheep.forms.birthday.placeholder')"
          icon="calendar-today"
          v-model="birthday"
          :disabled="!edit"
        />
      </b-field>
      <b-field :label="$t('pages.admin.sheep.forms.sex.label')">
        <div>
          <b-radio
            :disabled="!edit"
            v-model="sheep.sex"
            name="form-sex"
            native-value="M"
            >{{ $t('pages.admin.sheep.forms.sex.male') }}</b-radio
          >
          <b-radio
            :disabled="!edit"
            v-model="sheep.sex"
            name="form-sex"
            native-value="F"
            >{{ $t('pages.admin.sheep.forms.sex.female') }}</b-radio
          >
        </div>
      </b-field>
      <div v-if="edit">
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
import { mapState } from 'vuex'
import { showError } from '@/plugins/global'

export default {
  props: {
    value: Object,
    edit: {
      type: Boolean,
      default() {
        return false
      }
    }
  },
  data() {
    return {
      sheep: {},
      birthday: ''
    }
  },
  computed: {
    ...mapState('categories', ['categories']),
    ...mapState('breeds', ['breeds'])
  },
  async fetch() {
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
      this.edit = false
    },
    async save() {
      const url = `/api/v1/sheeps/${this.sheep.id}/`
      this.sheep.birthday = this.birthday.toLocaleDateString('fr-CA')
      try {
        await this.$axios['patch'](url, this.sheep)
        this.$toasted.global.defaultSuccess()
      } catch (e) {
        showError(e)
      }
    }
  }
}
</script>

<style></style>
