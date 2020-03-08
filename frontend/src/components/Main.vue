<template>
    <div class="container" >
      <!-- Projects -->
      <div class="row">
      <div class="col-sm-12">
        <h1>Projects</h1>
<button type="button" class="btn btn-success btn-sm" v-b-modal.project-modal>Add Project</button>
        <hr><br>
        <alert :message="message" v-if="showMessage"></alert>
        <div class= "row d-inline-flex">
          <div class="card" style="width:18rem; margin:10px auto " v-for="(project, index) in projects" :key="index">
            <img v-bind:src="project.url" class="card-img-top" style="" alt="...">
            <div class="card-body">
              <h5 class="card-title">{{project.title}}</h5>
              <p class="card-text">{{project.info}}</p>
              <button type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.project-update-modal
                        @click="editProject(project)">
                  Update
                </button>
                <button type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteProject(project)">
                  Delete
                </button>
            </div>
        </div>
        </div>
      </div>
      </div>
      <!-- Add project -->
      <b-modal ref="addProjectModal"
             id="project-modal"
             title="Add a new project"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addProjectForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-info-group"
                      label="Info:"
                      label-for="form-info-input">
            <b-form-input id="form-info-input"
                          type="text"
                          v-model="addProjectForm.info"
                          required
                          placeholder="Enter info">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-url-group"
                      label="Photo url:"
                      label-for="form-url-group">
            <b-form-input id="form-url-input"
                          type="text"
                          v-model="addProjectForm.url"
                          required
                          placeholder="Enter photo url">
            </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
      <!-- Edit project -->
    <b-modal ref="editProjectModal"
             id="project-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
      <b-form-input id="form-title-edit-input"
                    type="text"
                    v-model="editProjectForm.title"
                    required
                    placeholder="Enter title">
      </b-form-input>
      </b-form-group>
      <b-form-group id="form-info-edit-group"
                    label="Info:"
                    label-for="form-info-edit-input">
        <b-form-input id="form-info-edit-input"
                      type="text"
                      v-model="editProjectForm.info"
                      required
                      placeholder="Enter info">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-url-edit-group"
                    label="Photo Url:"
                    label-for="form-url-edit-input">
        <b-form-input id="form-url-edit-input"
                      type="text"
                      v-model="editProjectForm.url"
                      required
                      placeholder="Enter url">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Update</b-button>
      <b-button type="reset" variant="danger">Cancel</b-button>
    </b-form>
    </b-modal>
    </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      projects: [],
      addProjectForm: {
        title: '',
        info: '',
        url: '',
      },
      news: [],
      message: '',
      showMessage: false,
      editProjectForm: {
        id: '',
        title: '',
        info: '',
        url: '',
      },
    };
  },
  methods: {
    getProjects() {
      const path = 'http://localhost:5000/projects';
      axios.get(path)
        .then((res) => {
          this.projects = res.data.projects;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error);
        });
    },
    addProject(payload) {
      const path = 'http://localhost:5000/projects';
      axios.post(path, payload)
        .then(() => {
          this.getProjects();
          this.message = 'Project added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.log(error);
          this.getProjects();
        });
    },
    initForm() {
      this.addProjectForm.title = '';
      this.addProjectForm.info = '';
      this.addProjectForm.url = '';
      this.editProjectForm.title = '';
      this.editProjectForm.info = '';
      this.editProjectForm.url = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addProjectModal.hide();
      const payload = {
        title: this.addProjectForm.title,
        info: this.addProjectForm.info,
        url: this.addProjectForm.url,
      };
      this.addProject(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addProjectModal.hide();
      this.initForm();
    },
    editProject(project) {
      this.editProjectForm = project;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editProjectModal.hide();
      const payload = {
        title: this.editProjectForm.title,
        info: this.editProjectForm.info,
        url: this.editProjectForm.url,
      };
      this.updateProject(payload, this.editProjectForm.id);
    },
    updateProject(payload, projectID) {
      const path = `http://localhost:5000/projects/${projectID}`;
      axios.put(path, payload)
        .then(() => {
          this.getProjects();
          this.message = 'Project updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error);
          this.getProjects();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editProjectModal.hide();
      this.initForm();
      this.getProjects();
    },
    removeProject(projectID) {
      const path = `http://localhost:5000/projects/${projectID}`;
      axios.delete(path)
        .then(() => {
          this.getProjects();
          this.message = 'Project removed!';
          this.showMessage = true;
        })
        .catch((error) => {
        // eslint-отключение следующей строки
          console.error(error);
          this.getProjects();
        });
    },
    onDeleteProject(project) {
      this.removeProject(project.id);
    },
  },
  components: {
    alert: Alert,
  },
  created() {
    this.getProjects();
  },
};
</script>

<style scoped>

</style>
