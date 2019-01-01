program main

    use param

    use calc_basel

    implicit none

    real :: threshhold

    print *, "enter threshhold as a real number: "
    read *, threshhold

    call calcBasel(threshhold)
   

end program main
