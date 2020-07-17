<template>
  <form action="">
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Novo Aninal</p>
      </header>
      <section class="modal-card-body">
        <b-field
          :label="$t('pages.admin.sheep.forms.earringNumber.label')"
          message="Código do brinco"
          horizontal
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
        <b-field :label="$t('pages.admin.sheep.forms.breed.label')" horizontal>
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
          horizontal
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
          horizontal
        >
          <b-datepicker
            v-model="birthday"
            :placeholder="$t('pages.admin.sheep.forms.birthday.placeholder')"
            icon="calendar-today"
          />
        </b-field>
        <b-field
          :label="$t('pages.admin.sheep.forms.sex.label')"
          class="has-check"
          horizontal
        >
          <radio-picker
            v-model="sheep.sex"
            :options="{
              M: $t('pages.admin.sheep.forms.sex.male'),
              F: $t('pages.admin.sheep.forms.sex.female')
            }"
          ></radio-picker>
        </b-field>
        <b-field
          :label="$t('pages.admin.sheep.forms.teethQuantity.label')"
          horizontal
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
        <b-field horizontal>
          <b-field grouped>
            <div class="control">
              <b-button native-type="submit" type="is-primary">{{
                $t('buttons.save')
              }}</b-button>
            </div>
            <div class="control">
              <b-button
                type="is-primary is-outlined"
                @click.prevent="$parent.close()"
                >{{ $t('buttons.reset') }}</b-button
              >
            </div>
          </b-field>
        </b-field>
      </section>
    </div>
  </form>
</template>

<script>
import { mapState, mapActions } from 'vuex'
// import RadioPicker from '@/components/templates/RadioPicker'
export default {
  // components: {RadioPicker},
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
