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
    <div class="tile is-parent">
      <div class="tile is-child is-3">
        <strong>Permissões</strong>
      </div>
      <div class="tile is-child is-9 permissions">
        <div class="select-perms">
          <b-field>
            <b-select multiple size="10" native-size="10" v-model="selectPermissionsFrom">
              <option
                v-for="permission in permissions_core"
                :key="permission.id"
                :value="permission.id"
              >{{permission.name}}</option>
            </b-select>
          </b-field>
          <b-button
            type="is-info"
            @click="selectAllPerm"
            icon-right="arrow-right-bold-outline"
          >Escolher todos</b-button>
        </div>
        <div class="select-buttons">
          <b-button type="is-info" @click="selectPerm" icon-right="arrow-right-bold-outline"></b-button>
          <b-button type="is-info" @click="removePerm" icon-right="arrow-left-bold-outline"></b-button>
        </div>
        <div class="select-perms">
          <b-field>
            <b-select multiple native-size="10" v-model="selectPermissionsTo">
              <option
                v-for="permission in choosed_permissions"
                :key="permission.id"
                :value="permission.id"
              >{{permission.name}}</option>
            </b-select>
          </b-field>
          <b-button
            type="is-info"
            @click="removeAllPerm"
            icon-right="arrow-left-bold-outline"
          >Remover todos</b-button>
        </div>
      </div>
    </div>

    <div class="form-bottons columns is-mobile is-centered">
      <div class="column is-3">
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
  data() {
    return {
      selectPermissionsFrom: [],
      selectPermissionsTo: [],
      choosedIds: [],
      group: {},
      permissions: [],
      originalGroup: {}
    }
  },
  async fetch() {
    this.group = this.$route.params.group
    Object.assign(this.originalGroup, this.group)
    this.permissions = await this.$axios.$get("/api/v1/permissions/");
    this.choosedIds= this.group.permissions.map( ({id}) => id)
  },
  computed: {
    permissions_core() {
      let choosed = this.choosedIds

      var perms = this.permissions.filter(function(permission) {
        return (
          (permission.content_type.startsWith('core') || permission.content_type.startsWith('auth')) &&
          (choosed.includes(permission.id) == false)
        );
      });
      return perms;
    },
    choosed_permissions() {
      let choosed = this.choosedIds
      var perms = this.permissions.filter(function(permission) {
        return choosed.includes(permission.id)
      });
      return perms;
    }
  },


  methods: {
    reset() {
      Object.assign(this.group, this.originalGroup)
    },
    selectPerm() {
      this.choosedIds = [ ...this.choosedIds, ...this.selectPermissionsFrom]
      this.selectPermissionsFrom = []
    },
    selectAllPerm() {
      this.choosedIds = [ ...this.choosedIds, ...this.permissions_core.map( ({id}) => id)]
      this.selectPermissionsFrom = []
    },
    removePerm() {
      this.choosedIds = this.choosedIds.filter( (id) => !this.selectPermissionsTo.includes(id))
      this.selectPermissionsTo = []
    },
    removeAllPerm() {
      this.choosedIds = []
      this.selectPermissionsTo = []
    },
    save() {
      const id = this.group.id
      console.log(this.group)
      console.log(this.choosedIds)
      this.group.permissions = this.choosedIds
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
.permissions {
  display: flex;
  height: 400px;
}
.select-perms {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 40%;
}

.select-buttons {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin-top: 100px;
}

.select-buttons button {
  margin-bottom: 10px;
}
</style>
