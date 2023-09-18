function sendEmail() {
  var mail = document.getElementById("send_message").innerHTML;
  var subject = "New Opportunity";
  var mailtoLink =
    "mailto:tuananh.chu1995@gmail.com" +
    "?subject=" +
    subject +
    "&body=" +
    mail;
  window.location = mailtoLink;
}

const { createApp, ref } = Vue;

const app_CV = createApp({
  data() {
    return {
      userLoggedIn: true, // Simulate user login status
    };
  },
});

app_CV.mount("#CV");

//Creating VUE App for using array to store my infomation
const app = createApp({
  data() {
    return {
      user: [
        {
          phone: "0402 466 247",
          email: "tuananh.chu1995@gmail.com",
          address: "4 Hanleth Ave, Springvale VIC 3171",
        },
      ],
    };
  },
});
app.mount("#app");

const create_about = createApp({
  data() {
    return {
      about: [
        "I have built my career around vast IT knowledge and customer services, combine with strong communication skills and an energetic attitude. It allows me to be a team player, help support my team, and identify and create solutions within businesses. From technical issues with tools or equipment to a client inquiry, I know my team can count on me.",
        "IT in general is changing consistently, with new technologies and applications being developed every day. And I want to be a part of it, I want to expand my skills and experiences within it. To me, it is never too late to learn and there would be always space for improvement. It could be in a classroom setup, but nothing can beat a hand on experience.",
      ],
    };
  },
});
create_about.mount("#about_me");

const create_skill = createApp({
  data() {
    return {
      skills: [
        "Digital Marketing",
        "Stock/ Inventory Management",
        "Excel/Word - Office Suite",
        "Software Developer: HTML, C++, Python",
        "Database Managment MySQL",
      ],
    };
  },
});
create_skill.mount("#skills");

const create_project = createApp({
  data() {
    return {
      projects: [
        "Online Price Scrapping for All Modile ",
        "Auto Pictures to PDF converter for eReader",
        "Excel/Word - Office Suite",
        "Software Developer: HTML, C++, Python",
        "Database Managment MySQL",
      ],
    };
  },
});
create_project.mount("#project");

const create_education = createApp({
  data() {
    return {
      deakin: [
        {
          name: "Deakin University - Burwood Campus",
          start: "2023",
          end: "2026",
          course: "Bacholer Of Information Technology",
        },
      ],
      keysborough: [
        {
          name: "Keysborough College",
          start: "2012",
          end: "2015",
          course: "Year 12",
          ATAR: "76",
        },
      ],
      apple: [
        {
          name: "Apple Certificated Technician",
          start: "2021",
        },
      ],
    };
  },
});
create_education.mount("#education");

// Create a Vue app instance called "display_message."
const display_message = createApp({
  // Define the data function.
  data() {
    // Create a reactive variable called client_number and client_email
    const client_number = ref("");
    const client_email = ref("");
    // Return an object containing the "message" variable.
    return {
      client_number,
      client_email,
    };
  },
});
// Mount the "display_message" app instance to an HTML element with the id "app2" in the main HTML body.
display_message.mount("#your_detail");

//Working With Vue Route

// 1. Define route components.
// These can be imported from other files
const ProjectConverter = {
  template:
    "<h3>Price Scrap For All Phones Available On Mobile Monster</h3><p>Perform price scrappping bases on a pre-existance list of SKU and URL</p>",
};
const ProjectPDF = {
  template:
    "<h3>Convert Pictures Within Folder into PDF</h3><p>Making PDF from pictures for eReader</p>",
};
const MiniGame = {
  template: "<h3>Mini Space Game</h3><p>Code From C++</p>",
};
// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
  { path: "/", component: ProjectConverter },
  { path: "/ProjectOne", component: ProjectPDF },
  { path: "/ProjectTwo", component: MiniGame },
];

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = VueRouter.createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: VueRouter.createWebHashHistory(),
  routes, // short for `routes: routes`
});

// 5. Create and mount the root instance.
const app_2 = Vue.createApp({});

// Make sure to _use_ the router instance to make the
// whole app router-aware.
app_2.use(router);

app_2.mount("#projects");
