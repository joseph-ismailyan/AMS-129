program gauss

  implicit none

  real, dimension(3,3) :: A
  real, dimension(3) :: b

  real :: holder
  real :: holder2

  integer :: i,j

  ! initialize matrix A and vector b
  A(1,:) = (/2., 3., -1./)
  A(2,:) = (/4., 7., 1./)
  A(3,:) = (/7., 10., -4./)

  b = (/1., 3., 4./)

  ! print augmented matrix
  print *, "original matrix........."
  print *, "***********************" 
  do i = 1, 3           ! i is row
    print *, A(i,:), "|", b(i)
  end do

    do i = 2, 3
      ! STUDENTS: PLEASE FINISH THIS GAUSSIAN ELIMINATION
      ! for some reason doing this in 
      ! the b(i) assignment
      ! would result in no change
      holder = (-A(i,1)/A(1,1))
      A(i,:) = A(i,:) + (A(1,:) * holder)
      b(i) = b(i) + (b(1) * holder)
    end do

  ! print augmented matrix again
  ! this should be an echelon form (or triangular form)
  print *, ""    ! print a blank line
  print *, "Gaussian elimination........"
  print *, "***********************"
  do i = 1, 3
    print *, A(i,:), "|", b(i)
  end do

  ! doing back substitution
  ! working on eliminating the third column
  do i = 1, 2! FINISH THIS LOOP        ! i is row
    ! STUDENTS: PLEASE FINISH THIS BACK SUBSTITUTION
    ! HINT: THIS PART IS PRETTY MUCH SIMILAR WITH GAUSSIAN ELIM. PART.
    holder = (-A(i,3)/A(3,3))
    A(i,:) = A(i,:) + (A(3,:) * holder)
    b(i) = b(i) + (b(3) * holder)
  end do

  ! working on eliminating the second column
  do j = 1,3,2
    holder2 = (-A(j,2)/A(2,2))
      A(j,:) = A(j,:) + (A(2,:) * holder2)
      b(j) = b(j) + (b(2) * holder2)
  end do



  print *, ""    ! print a blank line
  print *, "back subs......"

  

  ! print the results
  print *, "***********************"
  do i = 1, 3
    print *, A(i,:), "|", b(i)
  end do
 
  print *, ""
  print *, "The solutions are:"
  ! STUDENTS: PLEASE CALCULATE A SOLUTION VECTOR, AND PRINT TO THE SCREEN.
  do i=1,3
    print*, b(i)/A(i,i)
  end do



end program gauss