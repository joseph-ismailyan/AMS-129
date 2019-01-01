module euler

    implicit none

    public :: dydt

    contains

        function dydt(t,y) result(i)

            implicit none

            integer, parameter :: dp = selected_real_kind(14)

            real(kind = dp), intent(in) :: y !input
            real(kind = dp), intent(in) :: t !input
            real(kind = dp) :: i !output

            i = (2*t)/(y*(1+(t*t))) 

        end function dydt


        subroutine eulers_method(t_0, y_0, t_f, N, file_name)
            
            implicit none

            !double precision variable
            integer, parameter :: dp = selected_real_kind(14)

            real, intent(in) :: t_0 !t_0 : initial point of t
            real, intent(in) :: y_0 !y_0 : initial point of y
            real, intent(in) :: t_f !t_f : end point of t
            integer, intent(in) :: N !N : number of points
            character(*) :: file_name !file_name : name of output file
            
            real(kind = dp) :: delta_t !step size
            real(kind = dp) :: running_t !keeps track of t
            real(kind = dp) :: running_y !keeps track of y
            integer :: i !counter for do loop
            

            !initialize values
            delta_t = (abs(t_f) + abs(t_0))/(N-1) !interval divided by N
            running_t = t_0
            running_y = y_0


            !open file for writing
            open(1, file = file_name, status = 'replace')

            do i = 0, N-1
                running_t = (i*delta_t)
                write (1,*) running_t
                write(1,*) running_y
                running_y = (dydt(running_t, running_y) * delta_t) + running_y
            end do

        end subroutine eulers_method

end module euler









