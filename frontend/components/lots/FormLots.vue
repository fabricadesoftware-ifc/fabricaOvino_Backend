<template>
  <form @submit.prevent="submit">
    <input id="lots-id" v-model="lots.id" type="hidden" />
    <b-field
      :label="$t('pages.lots.table.description')"
      message="Descrição do lote"
      horizontal
    >
      <b-input
        v-model="lots.description"
        :placeholder="$t('pages.lots.forms.lot.placeholder')"
        type="text"
        icon="tag"
        required
      />
    </b-field>
    <v-datetime v-model="date" :label="$t('pages.lots.forms.dateTime.label')" />
    <b-field horizontal>
      <b-field grouped>
        <div class="control">
          <b-button native-type="submit" type="is-primary">{{
            $t('buttons.save')
          }}</b-button>
        </div>
        <div class="control">
          <b-button type="is-primary is-outlined" @click="reset">{{
            $t('buttons.reset')
          }}</b-button>
        </div>
      </b-field>
    </b-field>
  </form>
</template>

<script>
//import { mapActions } from 'vuex'
import VDatetime from '@/components/templates/VDatetime'

export default {
  components: { VDatetime },
  props: {
    value: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  data() {
    return {
      date: new Date(),
      lots: {},
      original: {}
    }
  },
  watch: {
    value(newValue) {
      this.original = { ...newValue }
      this.lots = newValue
      this.date = newValue.date
    },
    lots(newValue) {
      this.$emit('input', newValue)
    }
  },
  created() {
    if (this.value) {
      this.original = { ...this.value }
      this.lots = this.value
    }
  },
  methods: {
    //...mapActions('lots', ['getLots']),
    async submit() {
      this.reset('reload')
      alert('submit')
      /*try {
        const method = this.value.id ? 'put' : 'post'
        const id = this.value.id ? `/${this.value.id}` : ''
        const url = `/api/v1/lots${id}/`
        await this.$axios[method](url, this.value)
        this.$toasted.global.defaultSuccess()
        this.getLots()
        this.reset('reload')
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }*/
    },
    reset(mode) {
      this.lots = this.lots.id && mode != 'reload' ? this.original : {}
    }
  }
}
</script>

<style></style>
