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
          v-model="dateTime"
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
  </section>
</template>

<script>
//import { showError } from '@/plugins/global'
export default {
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
  /*async fetch() {
    this.shearing = {
      id: this.shearing.id,
      date: this.shearing.date,
      amountOfWool: this.shearing.amountOfWool
    }
    this.edit = false
  },*/
  data() {
    return {
      //shearing: {}
    }
  },
  methods: {
    reset() {
      this.edit = false
    },
    async save() {
      /*const url = `/api/v1/shearing/${this.shearing.id}/`
      this.shearing.date = this.date.toLocaleDateString('fr-CA')
      try {
        await this.$axios['patch'](url, this.shearing)
        this.$toasted.global.defaultSuccess()
      } catch (e) {
        showError(e)
      }*/
      alert('Save')
    }
  }
}
</script>

<style></style>
