<template>
  <section>
    <PageTitle
      icon="scissors-cutting"
      :main="$t('pages.pagetitle.shearing_edit.title')"
      :sub="$t('pages.pagetitle.sheep_edit.subtitle')"
    />
    <b-tabs>
      <b-tab-item :label="$t('pages.pagetitle.shearing_edit.title')">
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
          <input id="shearing-id" v-model="shearing" type="hidden" />
          <b-field :label="$t('pages.admin.shearing.forms.amountOfWool')">
            <b-numberinput
              v-model="shearing.amountOfWool"
              controls-position="compact"
              controls-rounded
              step="0.01"
              :disabled="!edit"
              required
            ></b-numberinput>
          </b-field>

          <b-field :label="$t('pages.admin.shearing.forms.dateTime.label')">
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
import { showError } from '@/plugins/global'
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
  asyncData({ params }) {
    return {
      shearing: params.shearing
    }
  },
  data() {
    return {
      //shearing: {}
    }
  },
  methods: {
    reset() {
      this.shearing = {
        id: this.value.id,
        amountOfWool: this.value.amountOfWool,
        date: this.value.date
      }
      this.date = new Date(this.shearing.date)
      this.edit = false
    },
    async save() {
      const url = `/api/v1/shearing/${this.shearing.id}/`
      //this.shearing.date = this.date.toLocaleDateString('fr-CA')
      try {
        await this.$axios['patch'](url, this.shearing)
        this.$toasted.global.defaultSuccess()
        this.edit = false
      } catch (e) {
        showError(e)
      }
    }
  }
}
</script>

<style></style>
