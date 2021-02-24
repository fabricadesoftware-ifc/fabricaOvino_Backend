<template>
  <section>
    <PageTitle
      icon="sheep"
      :main="$t('pages.pagetitle.birth_edit.title')"
      :sub="$t('pages.pagetitle.sheep_edit.subtitle')"
    />
    <b-tabs>
      <b-tab-item :label="$t('pages.pagetitle.birth_edit.title')">
        <b-button
          v-if="edit"
          type="is-dark"
          icon-left="redo"
          @click="reset()"
          >{{ $t('buttons.reset') }}</b-button
        >
        <b-button
          v-else
          type="is-warning"
          icon-left="pencil"
          @click="edit = !edit"
          >{{ $t('buttons.edit') }}</b-button
        >
        <router-link to="/pt/sheeps/history" class="button">
          Voltar
        </router-link>
        <hr />
        <div class="form">
          <input id="births-id" v-model="birth" type="hidden" />

          <b-field>
            <b-input type="text" placeholder="Observações" icon="tag" />
          </b-field>

          <b-field
            :label="$t('pages.birth.forms.newbornsQuantity.placeholder')"
          >
            <b-numberinput
              v-model="birth.newborns_quantity"
              controls-position="compact"
              controls-rounded
              :disabled="!edit"
            ></b-numberinput>
          </b-field>

          <b-field :label="$t('pages.birth.forms.dateTime.label')">
            <b-datetimepicker
              v-model="date"
              icon="calendar-today"
              :disabled="!edit"
            ></b-datetimepicker>
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
      </b-tab-item>
    </b-tabs>
  </section>
</template>

<script>
//import { showError } from '@/plugins/global'
import PageTitle from '@/components/templates/PageTitle'
export default {
  components: { PageTitle },
  props: {
    value: {
      type: Object,
      default() {
        return {}
      }
    },
    edit: {
      type: Boolean,
      default() {
        return false
      }
    }
  },
  async fetch() {
    this.date = new Date(this.birth.date)
  },
  asyncData({ params }) {
    return {
      birth: params.birth
    }
  },
  data() {
    return {
      date: ''
    }
  },
  methods: {
    reset() {
      this.birth = {
        id: this.value.id,
        newborns_quantity: this.value.newborns_quantity,
        observations: this.value.observations,
        date: this.value.date
      }
      this.date = new Date(this.birth.date)
      this.edit = false
    }
    /*async save() {
      const url = `/api/v1/birth/${this.birth.id}/`
      this.birth.date = this.date.toLocaleDateString('fr-CA')
      try {
        await this.$axios['patch'](url, this.birth)
        this.$toasted.global.defaultSuccess()
        this.edit = false
      } catch (e) {
        showError(e)
      }
    }*/
  }
}
</script>

<style></style>
