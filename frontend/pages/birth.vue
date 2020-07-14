<template>
  <div class="birth">
    <PageTitle
      icon="lightbulb-outline"
      :main="$t('pages.birth.title')"
      :sub="$t('pages.birth.subtitle')"
    />
    <ValidationObserver ref="observer" v-slot="{ handleSubmit }">
      <div class="form">
        <b-tabs>
          <b-tab-item :label="$t('pages.birth.tabs.main')">
            <v-select
              :placeholder="$t('pages.birth.forms.sheep.placeholder')"
              icon="sheep"
              rules="required"
              :label="$t('pages.birth.forms.sheep.label')"
              :value="form.sheep"
              :readonly="mode === 'remove'"
              @input="updateSheep"
            >
              <option
                v-for="sheep in sheeps"
                :key="sheep.id"
                :value="sheep.id"
                >{{ sheep.earringNumber }}</option
              >
            </v-select>
            <b-field
              :label="$t('pages.birth.forms.dateTime.label')"
              class="pregnancyDiagnosis-form-fields"
            >
              <b-datetimepicker
                v-model="form.date"
                :placeholder="$t('pages.birth.forms.dateTime.placeholder')"
                icon="calendar-today"
                :readonly="mode === 'remove'"
              >
                <template v-slot:left>
                  <button
                    class="button is-primary"
                    @click="datetime = new Date()"
                  >
                    <b-icon icon="clock"></b-icon>
                    <span>Now</span>
                  </button>
                </template>
                <template v-slot:right>
                  <button class="button is-danger" @click="datetime = null">
                    <b-icon icon="close"></b-icon>
                    <span>Clear</span>
                  </button>
                </template>
              </b-datetimepicker>
            </b-field>
            <b-field
              :label="$t('pages.birth.forms.newbornsQuantity.label')"
              class="birth-form-fields"
            >
              <b-numberinput
                rounded
                :placeholder="
                  $t('pages.birth.forms.newbornsQuantity.placeholder')
                "
                icon="mdi-tooth"
                min="0"
                max="5"
                :value="form.newborns_quantity"
                :readonly="mode === 'remove'"
                @input="updateNewbornsQuantity"
              />
            </b-field>
          </b-tab-item>

          <b-tab-item
            v-for="(newborn, index) in form.newborns"
            :key="index"
            :label="$t('pages.birth.tabs.newborn') + ' ' + (+index + 1)"
          >
            <newborn :newborn="newborn" :index="index" />
          </b-tab-item>
        </b-tabs>
        <input id="birth-id" v-model="pregnancyDiagnosis.id" type="hidden" />

        <div class="sheep-form-buttons">
          <b-button
            v-if="mode === 'save'"
            type="is-info"
            icon-left="check"
            @click.prevent="handleSubmit(save)"
            >{{ $t('buttons.save') }}</b-button
          >
          <b-button
            v-else
            type="is-danger"
            icon-left="trash-can-outline"
            @click="remove"
            >{{ $t('buttons.delete') }}</b-button
          >
          <b-button type="is-dark" icon-left="redo" @click="reset">{{
            $t('buttons.reset')
          }}</b-button>
        </div>
      </div>
    </ValidationObserver>
    <hr />
  </div>
</template>

<script>
import { ValidationObserver } from 'vee-validate'
import PageTitle from '@/components/templates/PageTitle'
import VSelect from '@/components/templates/VSelect'
import Newborn from '@/components/birth/Newborn'
import { mapState } from 'vuex'
export default {
  components: { Newborn, PageTitle, VSelect, ValidationObserver },
  computed: {
    ...mapState('birth', ['form']),
    ...mapState('auth', ['user'])
  },
  async fetch() {
    this.users = await this.$axios.$get('/api/v1/users')
    this.sheeps = await this.$axios.$get('/api/v1/sheeps/?pregnant=True')
  },
  data() {
    return {
      mode: 'save',
      number: 0,
      date: new Date(),
      pregnancyDiagnosis: {},
      sheeps: [],
      users: [],
      pregnancyDiagnostics: []
    }
  },

  created() {
    if (!this.form.date) {
      this.updateDate(new Date())
    }
  },
  methods: {
    updateSheep(value) {
      this.$store.commit('birth/sheep', value)
    },
    updateDate(value) {
      this.$store.commit('birth/date', value)
    },
    updateNewbornsQuantity(value) {
      if (value > this.form.newborns_quantity) {
        let diff = value - this.form.newborns_quantity
        this.$store.commit('birth/addNewborns', { value, diff })
      } else {
        let diff = this.form.newborns_quantity - value
        this.$store.commit('birth/removeNewborns', { value, diff })
      }
    },
    reset() {
      this.$store.commit('birth/reset')
      this.mode = 'save'
      this.$fetch()
    },
    save() {
      this.form.user = this.user.id
      this.form.birthday = this.form.date.toLocaleDateString('fr-CA')
      this.form.date = this.form.date.toISOString()

      // const method = this.sheep.id ? "put" : "post";
      // const id = this.sheep.id ? `/${this.sheep.id}` : "";
      // const url = `/api/v1/sheeps${id}/`;
      // this.sheep.birthday = this.birthday.toLocaleDateString('fr-CA')
      // console.log(this.sheep)
      this.$axios
        .$post('/api/v1/births/', this.form)
        .then(() => {
          this.$toasted.global.defaultSuccess()
          this.reset()
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
