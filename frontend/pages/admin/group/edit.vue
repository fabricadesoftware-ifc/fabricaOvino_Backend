<template>
  <div class="group-edit">
    <PageTitle
      icon="face"
      :main="$t('pages.admin.group.edit.title')"
      :sub="$t('pages.admin.group.edit.subtitle')"
    />

    <div class="tile is-parent">
      <div class="tile is-child is-3">
        <strong>Configurações gerais</strong>
      </div>
      <div class="tile is-child is-8">
        <input type="hidden" id="group-id" v-model="group.id" />
        <b-field :label="$t('pages.admin.forms.name.label')" class="group-form-fields">
          <b-input
            :placeholder="$t('pages.admin.forms.name.placeholder')"
            type="text"
            icon="tag"
            v-model="group.name"
            required
          />
        </b-field>
      </div>
    </div>

    <div class="form-bottons columns is-mobile is-centered">
      <div class="column is-4">
        <b-button type="is-info" icon-left="check" @click="save">{{ $t('buttons.save') }}</b-button>
        <b-button type="is-dark" icon-left="redo" @click="reset">{{ $t('buttons.reset') }}</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import { showError } from '@/plugins/global'
export default {
  components: { PageTitle },
  fetch() {
    this.group = this.$route.params.group
    Object.assign(this.originalGroup, this.group)
  },
  data() {
    return {
      group: {},
      originalGroup: {}
    }
  },

  methods: {
    reset() {
      Object.assign(this.group, this.originalGroup)
    },
    save() {
      const id = this.group.id
      const url = `/api/v1/groups/${id}/`
      this.$axios
        .$put(url, this.group)
        .then(res => {
          this.$toasted.global.defaultSuccess()
          this.reset()
          sthis.group = res
        })
        .catch(showError)
    }
  }
}
</script>

<style>
.form-bottons {
  margin-top: 20px;
}
</style>
