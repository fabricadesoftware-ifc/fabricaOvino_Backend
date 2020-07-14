<template>
  <form action="">
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Novo Aninal</p>
      </header>
      <section class="modal-card-body">
        <b-field
          :label="$t('pages.admin.sheep.forms.earringNumber.label')"
          class="sheep-form-fields"
        >
          <b-input
            v-model="sheep.earringNumber"
            :placeholder="
              $t('pages.admin.sheep.forms.earringNumber.placeholder')
            "
            type="text"
            icon="tag"
            required
          />
        </b-field>
        <b-field
          :label="$t('pages.admin.sheep.forms.breed.label')"
          class="sheep-form-fields"
        >
          <b-select
            v-model="sheep.breed"
            :placeholder="$t('pages.admin.sheep.forms.breed.placeholder')"
            icon="puzzle"
            required
          >
            <option v-for="breed in breeds" :key="breed.id" :value="breed.id">{{
              breed.name
            }}</option>
          </b-select>
        </b-field>
        <b-field
          :label="$t('pages.admin.sheep.forms.category.label')"
          class="sheep-form-fields"
        >
          <b-select
            v-model="sheep.category"
            :placeholder="$t('pages.admin.sheep.forms.category.placeholder')"
            icon="alpha-c-circle-outline"
            required
          >
            <option
              v-for="category in categories"
              :key="category.id"
              :value="category.id"
              >{{ category.name }}</option
            >
          </b-select>
        </b-field>
        <b-field
          :label="$t('pages.admin.sheep.forms.birthday.label')"
          class="sheep-form-fields"
        >
          <b-datepicker
            v-model="birthday"
            :placeholder="$t('pages.admin.sheep.forms.birthday.placeholder')"
            icon="calendar-today"
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
        <b-field
          :label="$t('pages.admin.sheep.forms.teethQuantity.label')"
          class="sheep-form-fields"
        >
          <b-numberinput
            v-model="sheep.teethQuantity"
            rounded
            :placeholder="
              $t('pages.admin.sheep.forms.teethQuantity.placeholder')
            "
            icon="mdi-tooth"
            required
          />
        </b-field>
        <div class="sheep-form-buttons">
          <b-button type="is-info" icon-left="check" @click="save">{{
            $t('buttons.save')
          }}</b-button>
          <b-button type="is-dark" icon-left="redo" @click="$parent.close()">{{
            $t('buttons.reset')
          }}</b-button>
        </div>
      </section>
    </div>
  </form>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  data() {
    return {
      birthday: new Date(),
      sheep: {
        teethQuantity: 0
      }
    }
  },
  computed: {
    ...mapState('breeds', ['breeds']),
    ...mapState('categories', ['categories'])
  },
  methods: {
    ...mapActions('sheeps', ['getSheeps']),
    async save() {
      this.sheep.birthday = this.birthday.toLocaleDateString('fr-CA')
      const url = `/api/v1/sheeps/`

      try {
        await this.$axios.post(url, this.sheep)
        this.$toasted.global.defaultSuccess({
          msg: 'Operação realizada com sucesso'
        })
        this.getSheeps()
        this.$parent.close()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    }
  }
}
</script>

<style></style>
