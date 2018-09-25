'use strict';
 
var gulp = require('gulp');
var sass = require('gulp-sass');
 
 //compile sass
gulp.task('sass-compiler', function () {
  return gulp.src('./scss/**/*.scss')
    .pipe(sass({
      outputStyle: 'expended'
    }).on('error', sass.logError))
    .pipe(gulp.dest('./css'));
});
 
 //compile and watch
gulp.task('sass', function () {
  gulp.watch('./scss/**/*.scss', ['sass-compiler']);
});