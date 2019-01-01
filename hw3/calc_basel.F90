module calc_basel
    !implicit none

    use param

    real(kind = 8) :: basel = 1.
    real(kind = 8) :: error
    integer :: denominator = 1
    real(kind = 8) :: steps = 1.
    
    contains

    subroutine calcBasel(threshhold)

        ! calculates basel formula to given threshhold
        ! using param module to find (pi**2)/6

        implicit none

        real :: threshhold


        error = abs(((pi**2)/6)-basel)
        ! calculate first basel number
        ! assign a value to error

        print *, "This might take a while.."
		
        open(1, file = 'results.txt', status = 'replace')        
        do while (error > threshhold)
            ! print 'steps' every 1000 iterations
            !print *, steps, pi, basel, error
            steps = steps + 1
            basel = basel + (1/steps**2)
            error = abs(((pi**2)/6)-basel)
            !print *, error

            if (mod(steps,1000.) .eq. 0) then
                !print *, "step = ", steps
                write (1,*) "step = ", steps, achar(10), "error = ", error, achar(10), achar(10)
            end if
        end do
        close(1)
        print *, "steps = ", steps, achar(10)
        print *, "solution = ", basel, achar(10)
        print *, "error = ", error

        write (1,*) "total steps = ", steps, achar(10)
        write (1,*) "solution = ", basel, achar(10)
        write (1,*) "error = ", error

    end subroutine calcBasel

end module calc_basel
